import psycopg2

#used for all three options to connect to the database and set up cursur
def connect_db():
	myConnection = psycopg2.connect( host='localhost', 
		user='ENTER_HERE', 
		password='ENTER_HERE', 
		dbname='news')
	return myConnection

#used to Create Selection #1 for viewing the top three articles
def article_views(cur):
	views_query = '''
		create view article_views as 
			select replace(path, '/article/', '') as article_slug,
			count(*) as total_views
			from log where status = '200 OK'
			group by article_slug
			order by total_views
	'''
	cur.execute(views_query)

def popular_articles():
	db = connect_db()
	cur = db.cursor()
	article_views(cur)
	query = '''select title, total_views
		from articles, article_views
		where slug = article_slug
		order by total_views desc
		limit 3'''
	cur.execute(query)
	print('TOP THREE MOST VIEWED ARTICLES:\n')
	for title, total_views in cur.fetchall():
		print('''   Article Title: {}
	   Total Views: {}

		'''.format(title, format(total_views, ",d")))
	db.close()

def popular_authors():
	db = connect_db()
	cur = db.cursor()
	article_views(cur)
	query = '''select authors.name,
		sum(article_views.total_views) as ttl_auth_views
		from articles, article_views, authors 
		where articles.slug = article_views.article_slug 
		and articles.author = authors.id
		group by authors.name
		order by ttl_auth_views desc'''
	cur.execute(query)
	print('MOST POPULAR AUTHORS:\n')
	for title, total_views in cur.fetchall():
		print('''   Author Name: {}
	   Total Views: {}

		'''.format(title, format(int(total_views), ",d")))
	db.close()

def errors():
	db = connect_db()
	cur = db.cursor()
	article_views(cur)
	query = '''
	select total_requests.date,
	cast(with_error.total as float) / cast(total_requests.total as float) * 100 as percent_errors
	from (
		select to_char(time, 'mm-dd-yyyy') as date,
			count(*) as total from log
			group by date
	) as total_requests, (
		select to_char(time, 'mm-dd-yyyy') as date,
			count(*) as total from log
			where cast(left(status,3) as int) >= 400
			group by date
	) as with_error
	where total_requests.date = with_error.date AND
	cast(with_error.total as float) / cast(total_requests.total as float) * 100 > 1
	'''
	cur.execute(query)

	print("Days which had total page requests that were greater than 1%:\n")
	for date, percentage in cur.fetchall():
		print('''Date: {}
Percentage: {}%
		'''.format(date, round(percentage, 2)))
	db.close()