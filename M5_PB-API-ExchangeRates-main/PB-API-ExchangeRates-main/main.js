console.log('Hello world!')

const ws = new WebSocket('ws://localhost:8080')

const formChat = document.getElementById('formChat')
const textField = document.getElementById('textField')
const subscribe = document.getElementById('subscribe')

formChat.addEventListener('submit', async (e) => {
    e.preventDefault()
    const message = textField.value.trim()

    if (message.startsWith('exchange')) {
        ws.send(message.startsWith('exchange ') ? message : 'exchange ' + message)
        textField.value = null
    } else {
        alert('Невірний формат команди. Використовуйте "exchange <дні>" для перегляду курсів валют.')
    }
})

ws.onopen = (e) => {
    console.log('Hello WebSocket!')
}

ws.onmessage = async (e) => {
    const message = e.data;

    try {
        const data = JSON.parse(message); // Розпарсити отримане JSON-повідомлення

        if (Array.isArray(data)) {
            // Якщо дані - це масив, відобразити їх на сторінці
            data.forEach((item) => {
                const elMsg = document.createElement('div');
                elMsg.textContent = JSON.stringify(item, null, 2); // Відображення у вигляді тексту з форматуванням
                subscribe.appendChild(elMsg);
            });
        } else {
            // Вивести повідомлення як текст
            const elMsg = document.createElement('div');
            elMsg.textContent = message;
            subscribe.appendChild(elMsg);
        }
    } catch (error) {
        // Якщо не вдалося розпарсити JSON, вивести повідомлення як текст
        const elMsg = document.createElement('div');
        elMsg.textContent = message;
        subscribe.appendChild(elMsg);
    }
}
