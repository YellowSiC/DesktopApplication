from JsMeetsStarlette import JsMeetsPy
from starlette.routing import Route, Mount
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = JsMeetsPy(debug=True, static='static', templates='templates')

def add2(a, b):
    if a < 0 or b < 0:
        raise Exception('No negative arguments')
    return [a, b, a+b]


@app.route('/', ['GET'])
async def homepage(request):
    context = """
     function App() {
                return (
                    <div>
                        <Layout style={{ width: '400px',padding:'20px', background: '#fff' }}>
                            <Header style={{ background: '#fff', textAlign: 'center', padding: 0 }}>
                                <h1>Hello From ReactJs <EditOutlined /></h1>
                            <Content>
                                <Space direction="vertical">
                                    <Input placeholder="Placeholder text" style={{ width: 200 }} />
                                    <Button type="primary">Primary Button</Button>
                                    <Html5Outlined style={{ fontSize: '32px', color: '#08c' }} />
                                </Space>
                            </Content>
                        </Layout>
                    </div>
                );
            }
    
    """
    return app.templates.TemplateResponse('index.html', {'request': request, 
                                                         'main': context})

""" 
This library is modularized for each function. A sample case is introduced for each of the following four functions.

JsPyFunction : You can call python functions from javascript in a natural way. The reverse is also true.

JsPyQueue : You can send arbitrary data from javascript to the queue on the python side. The reverse is also true.

JsPyPubsub : Like MQTT, arbitrary data can be published/subscribed via the topic.

JsPyBinarySocket : Binary communication between client and server. 

"""