// src/api.ts

// Интерфейс для сообщений (если у вас его еще нет)
interface Message {
    text: string;
    imageUrl?: string;
    sender: "user" | "bot";
  }
  
  // Единая функция для отправки сообщения
export const sendMessage = async (text: string): Promise<Message> => {
  try {
    const response = await fetch('/api/message', {  // Новый endpoint!
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: text }), 
    });

    if (!response.ok) {
      throw new Error(`Ошибка HTTP: ${response.status}`);
    }

    const data = await response.json();
    return {
      text: data.message,
      imageUrl: data.imageUrl, // Если есть URL изображения
      sender: 'bot',
    }; 
  } catch (error) {
    console.error('Ошибка при отправке сообщения:', error);
    throw error;
  }
};