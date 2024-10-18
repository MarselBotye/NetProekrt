import { FC, useEffect, useState } from "react";
import "./App.css";
import Message from "./IMessage";
import MessageList from "./MessageList";
import MessageInput from "./MessageInput";
import { v4 as uuidv4 } from "uuid";
import { sendMessage } from './api';

const App: FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [sessionId, setSessionId] = useState<string>("");

  useEffect(() => {
    const currentUrl = window.location.href;
    const sessionMatch = currentUrl.match(/#([a-f0-9]{9,})/);
    const existingSessionId = sessionMatch ? sessionMatch[1] : null;

    if (existingSessionId) {
      setSessionId(existingSessionId); 
    } else {
      const newSessionId = uuidv4().replace(/-/g, '').substring(0, 10);
      setSessionId(newSessionId);
      window.history.replaceState(null, '', `#${newSessionId}`);
    }
  }, []);

  const handleSendMessage = async (text: string) => {
    setMessages([...messages, { text, sender: 'user' }]);
    setIsLoading(true);

    try {
      const botResponse = await sendMessage(text); 
      setMessages((prevMessages) => [...prevMessages, botResponse]); 
    } catch (error) {
      // ... обработка ошибок
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h2>Простой чат - ID: {sessionId}</h2>
      <MessageList messages={messages} isLoading={isLoading} />
      <MessageInput onSendMessage={handleSendMessage} />
    </div>
  );
};

export default App;