from aiohttp import web
import aiohttp_session
from jinja2 import Environment, FileSystemLoader
import variables

template = Environment(loader=FileSystemLoader('')).get_template('index.html')

async def index(request):
    """отрисовываем главную страницу"""
    context = {'op': 'title'}
    return web.Response(text=template.render(context),content_type='text/html')

async def handle_submit(request):
    """обрабатыеваем форму"""
    session = await aiohttp_session.get_session(request)
    session.clear()
    data = await request.post()
    print(data.get('name'))
    session['value'] = data.get('name')
    print(type(session),session.items())
    
    context = {
        'op':variables.op}
    return web.Response(text=template.render(context),content_type='text/html')

app = web.Application()
app.router.add_get('/',index)
app.router.add_post('/',handle_submit)
aiohttp_session.setup(app, aiohttp_session.SimpleCookieStorage())


if __name__=="__main__":
    web.run_app(app)



