from django.urls import reverse
from django.shortcuts import render
from . import util
from django.http import HttpResponseRedirect
from django import forms
from random import randint


# Importing the Markdown Entries so that we can retrieve them
import markdown2

# Create a new Class for Django Form
class CreateWikiForm(forms.Form):
    # Create 2 Input Fields for Name and Details
    wiki_name = forms.CharField(label="Name of New Wiki Page:")
    wiki_details = forms.CharField(
        label="Details about the New Wiki Page:", 
        # Setting Size of Textarea
        widget=forms.Textarea(
            attrs={ 'rows': 20,
                    'cols': 60,
                    'style': 'height: 50vh; display: block;'})
        )

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Creating a Route for the Entry Page
def entry(request, title):
    # Return the Markdown Content from the Page Requested
    requested_md = util.get_entry(title)
    # Validation to Ensure Markdown is not Empty
    if (requested_md == None):
        # Entry does not exist; Render an Error Page
        return render(request, "encyclopedia/error.html")
    
    # Convert the Markdown files into HTML
    markdowner = markdown2.Markdown()
    html_content = markdowner.convert(requested_md)

    return render(request, "encyclopedia/entry.html", {
        # Passing in Key-Value Pairs for Context
        "title" : title,
        "content" : html_content
    })

# Search Functionality
def search(request):
    # Get User Input
    query = request.GET['q']
    # Check if User's Query Terms is an Existing Page
    existing_entries = util.list_entries()
    if query in existing_entries:
        # If it is, determine the title the entry page
        queried_md = util.get_entry(query)
        if (queried_md == None):
            return render(request, "encyclopedia/error.html")
        # Redirect the User to the page they searched for
        else:
            return HttpResponseRedirect(reverse("encyclopedia:entry", args=[query]))
    
    # If the Query is not an Existing Page
    else:
        # List to hold related entries
        related_entries = []
        # Make the Query a Substring
        sub_string = str(query)
        # Check if Substring is part of the List of Entries (Strings) and add it to an empty list
        results = [substr for substr in existing_entries if sub_string in substr]
        # Append to our List of Related Entries
        related_entries += results
        # After Looping through all the available titles        
        return render(request, "encyclopedia/search.html", {
            "titles" : related_entries
        })

# Create a New Wiki Page
def create(request):
    if request.method == "POST":
        # Get Form Data from User, Key is referenced from the name of variables when we create the Class
        wiki_title = request.POST["wiki_name"]
        wiki_details = request.POST["wiki_details"]
        # Check if Created Page is Existing
        existing_entries = util.list_entries()
        if wiki_title in existing_entries:
            # Return an Error Message as Page is existing
            return render(request, "encyclopedia/create_error.html")
        
        # If Wiki Page is a New Page
        else:
            # Save New Wiki Page
            util.save_entry(wiki_title, wiki_details)
            # Redirect User to Newly Created Page
            return HttpResponseRedirect(reverse("encyclopedia:entry", args=[wiki_title]))


    
    # If User wants to go to Form Page
    else:
        # Return the Render of the Create HTML
        return render(request, "encyclopedia/create.html",{
            # But Pass in the Django Form we created
            "create_form": CreateWikiForm()
        })

# Editing an existing Wiki Page
def edit(request, title):
    if request.method == "POST":
        # Get User Input to Save
        wiki_details = request.POST["wiki_details"]

        # Save the Edits to the Page
        util.save_entry(title, wiki_details)
        # Redirect User to the edited page
        return HttpResponseRedirect(reverse("encyclopedia:entry", args=[title]  ))

    # GET Request to go to Edit Page
    else:
        # Get Markdown of the Page
        name = title
        markdown_files = util.get_entry(title)
        # Provide Initial Values for Existing Wiki Page
        existing_form = CreateWikiForm(initial={
            'wiki_name': title,
            'wiki_details': markdown_files
        })
        # Render the Template, Passing in our Form Data
        return render(request, "encyclopedia/edit.html", {
            'form': existing_form,
            'name': name
        })

# Providing the User with a Random Wiki Page
def random(request):
    # Get List of Entries
    existing_entries = util.list_entries()
    list_size = len(existing_entries)
    # Randomly Select one of the Existing Entries
    rand_index = randint(0, (list_size - 1))
    # Render the Selected Page
    selected_title = existing_entries[rand_index]
    selected_markdown = util.get_entry(selected_title)
    html = markdown2.markdown(selected_markdown)
    return render(request, "encyclopedia/entry.html", {
        'title': selected_title,
        'content': html
    })
