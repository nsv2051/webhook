// 把 bot888518123 改成自己的机器人就行,这个接口只有自己机器人的ID才会发送，不用担心呗滥用，BOTID没泄露就没事。。然后使用方法：

// https://xxxxx.xxx.workers.dev/bot888518123:***********************/sendMessage?chat_id=703019123&text=123

// 703019123 是自己的TG id

// 123 是内容

const whitelist = ["/bot888518123:"]; 
const tg_host = "api.telegram.org";

addEventListener('fetch', event => {
    event.respondWith(handleRequest(event.request))
})

function validate(path) {
    for (var i = 0; i < whitelist.length; i++) {
        if (path.startsWith(whitelist[i]))
            return true;
    }
    return false;
}

async function handleRequest(request) {
    var u = new URL(request.url);
    u.host = tg_host;
    if (!validate(u.pathname))
        return new Response('Unauthorized', {
            status: 403
        });
    var req = new Request(u, {
        method: request.method,
        headers: request.headers,
        body: request.body
    });
    const result = await fetch(req);
    return result;
}