from aiohttp import web
import aiohttp_session
from jinja2 import Environment, FileSystemLoader
import variables
from calculation import Evaluate, Token

template = Environment(loader=FileSystemLoader('')).get_template('index.html')

async def index(request):
    """отрисовываем главную страницу"""
    context = {'op': 'title'}
    return web.Response(text=template.render(context),content_type='text/html')

async def handle_submit(request):
    """обрабатыеваем форму"""
    session = await aiohttp_session.get_session(request)
    data = await request.post()
    if data.get('clear'):
        session['tmp'] , session['values'] = '',[]
    try:
        if Token(session.get('tmp') + data.get('value')):
            print(type(session.get('tmp')))
            session['tmp'] = session.get('tmp') + data.get('value')
        else:
            session['values'] += [session.get('tmp')]
            session['tmp'] = data.get('value')
            print('else',session.get('values'),[session.get('tmp')])
    except KeyError:
        print('key')
        session['tmp'] = data.get('value')
    except TypeError:
        print('type')
        session['tmp'] = data.get('value')
    context = {
        'op':variables.op}
    print(session.keys())
    return web.Response(text=template.render(context),content_type='text/html')

app = web.Application()
app.router.add_get('/',index)
app.router.add_post('/',handle_submit)
aiohttp_session.setup(app, aiohttp_session.SimpleCookieStorage())


if __name__=="__main__":
    web.run_app(app)



