// src/MessageInput.tsx

import React, { useState } from 'react';

interface MessageInputProps {
  onSendMessage: (message: string) => void; // Функция для отправки сообщений
}

const MessageInput: React.FC<MessageInputProps> = ({ onSendMessage }) => {
  const [message, setMessage] = useState('');

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    if (message.trim() !== '') {
      onSendMessage(message); // Отправляем сообщение в родительский компонент
      setMessage('');
    }
  };

  return (
    <div className="message-input">
      <input
        type="text"
        placeholder="Введите сообщение..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={handleSubmit}>Отправить</button>
    </div>
  );
};


export default MessageInput;
