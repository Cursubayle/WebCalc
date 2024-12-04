from aiohttp import web
from jinja2 import Environment, Template, FileSystemLoader
import variables

async def index(request):
    """отрисовываем главную страницу"""
    context = {'op': 'title'}
    env = Environment(loader=FileSystemLoader(''))
    template = env.get_template('index.html')
    return web.Response(text=template.render(context),content_type='text/html')

async def handle_submit(request):
    """обрабатыеваем форму"""
    context = {
        'op':variables.op}
    env = Environment(loader=FileSystemLoader(''))
    template = env.get_template('index.html')
    return web.Response(text=template.render(context),content_type='text/html')

app = web.Application()
app.router.add_get('/',index)
app.router.add_post('/submit',handle_submit)

if __name__=="__main__":
    web.run_app(app)



