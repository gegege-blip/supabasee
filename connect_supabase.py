from supabase import Client, create_client


def get_connect_supabase():
    url = 'https://xxwspyynilwyffycermx.supabase.co'
    api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh4d3NweXluaWx3eWZmeWNlcm14Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzQwOTg1NDIsImV4cCI6MjA0OTY3NDU0Mn0.t_S8cr6_6pIKorbl1TPQSoOqpQlMjloFAC2u88kRUNU'


    supabase = create_client(url, api_key)


    return supabase
