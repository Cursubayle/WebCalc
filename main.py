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
    try:
        print(session.get('values')[-1], data.get('value'))
        if Token(session.get('values')[-1] + data.get('value')):
            print(' if ')
            session['values'][-1] += 'a'
            # session['values'][-1] + 
            # (data.get('value'))
        else:
            print('else')
    except KeyError:
        print('key')
        session['values'] = list(data.get('value'))
    except TypeError:
        print('type')
        session['values'] = list(data.get('value'))
    context = {
        'op':variables.op}
    print(session.get('values'))
    return web.Response(text=template.render(context),content_type='text/html')

app = web.Application()
app.router.add_get('/',index)
app.router.add_post('/',handle_submit)
aiohttp_session.setup(app, aiohttp_session.SimpleCookieStorage())


if __name__=="__main__":
    web.run_app(app)



