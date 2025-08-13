document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('user-input-form');
    const input = document.getElementById('user-input');
    const chatLog = document.getElementById('chat-log');

    // Auto-focus al cargar
    input.focus();

    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        const message = input.value.trim();

        if (message) {
            appendMessage(message, 'user-message');

            try {
                const response = await fetch('/get_response', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ message })
                });

                const data = await response.json();

                if (data.response) {
                    appendMessage(data.response, 'bot-message');
                } else {
                    appendMessage('Lo siento, no entendí eso.', 'bot-message');
                }
            } catch (error) {
                appendMessage('Error al conectar con el servidor.', 'bot-message');
                console.error('Error:', error);
            }

            input.value = '';
            input.focus();
        }
    });

    function appendMessage(text, className) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', className);
        messageDiv.textContent = text;

        // Animación de entrada
        messageDiv.style.opacity = 0;
        messageDiv.style.transform = 'translateY(10px)';
        chatLog.appendChild(messageDiv);

        // Forzar reflow para activar transición
        void messageDiv.offsetWidth;

        messageDiv.style.transition = 'all 0.3s ease';
        messageDiv.style.opacity = 1;
        messageDiv.style.transform = 'translateY(0)';

        // Auto-scroll
        chatLog.scrollTop = chatLog.scrollHeight;
    }
});
