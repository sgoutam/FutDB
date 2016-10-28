__author__ = 'Rahul'
from flask import render_template, redirect, url_for
from app import app1
from .forms import SearchForm
from .dataHandle import worldcupplayers, eplteams
from TextSummarize import wiki_scrape

@app1.route('/' , methods=['GET', 'POST'])
@app1.route('/index' , methods=['GET', 'POST'])
def index():
    form = SearchForm()
    response = ''
    playerbool=True
    wiki_summary = ''
    if form.validate_on_submit():
        if form.searchChoice.data=='player':
            response = worldcupplayers(form.searchQuery.data)
            wiki_summary=wiki_scrape(form.searchQuery.data)
#           print(wiki_summary.summary)
            playerbool=True


        if form.searchChoice.data=='team':
            response = eplteams(form.searchQuery.data)
            wiki_summary=wiki_scrape(form.searchQuery.data)
            playerbool=False

        redirect(url_for('index'))
    return render_template('index.html',
                           form=form,
                           response=response,
                           playerbool=playerbool,
                           wiki_summary=wiki_summary)
