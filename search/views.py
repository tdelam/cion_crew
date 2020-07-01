import re
from django.shortcuts import render
from django.db.models import Q

from accounts.models import UserProfile


def search(request, template_name):
    query_string = ''
    results = UserProfile.objects.filter()

    if ('q' in request.GET) and request.GET['q'].strip() != '':
        query_string = request.GET['q']
        notes = 'user__skills__available_as'
        q_query = _get_query(query_string, [notes])
        results = results.filter(q_query).distinct()

    if ('location' in request.GET) and request.GET['location'].strip() != '':
        query_string = request.GET['location']
        location_query = _get_query(query_string, ['user__userprofile__city'])
        results = results.filter(location_query).distinct()

    if ('crew_position' in request.GET) and request.GET['crew_position'].strip() != '0':
        query_string = request.GET['crew_position']
        crew_position_query = _get_query(query_string, ['user__creditoptions__crew_position'])
        results = results.filter(crew_position_query).distinct()

    if ('project_name' in request.GET) and request.GET['project_name'].strip() != '':
        query_string = request.GET['project_name']
        project_name_query = _get_query(query_string, ['user__creditoptions__project_name'])
        results = results.filter(project_name_query).distinct()

    if ('affiliation' in request.GET) and request.GET['affiliation'].strip() != '':
        query_string = request.GET['affiliation']
        affiliation_query = _get_query(query_string, ['user__creditoptions__project_name'])
        results = results.filter(affiliation_query).distinct()

    results = results.order_by('user__last_name')

    return render(request, template_name, {
        'query_string': query_string,
        'results': results
    })


def _normalize_query(query_string, findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                     normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in individual keywords, getting rid of unnecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def _get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None  # Query to search for every search term
    terms = _normalize_query(query_string)
    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            # q = Q(**{"%s__iexact" % field_name: term})
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
