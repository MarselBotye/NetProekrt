import { FC } from "react";
import Message from "./IMessage";
import Spinner from "./spinner";

interface MessageListProps {
  messages: Message[];
  isLoading: boolean;
}

const MessageList: FC<MessageListProps> = ({ messages, isLoading }) => {
  return (
    <div className="message-list">
      {messages.map((message, index) => (
        <div
          key={index}
          className={`message ${
            message.sender === "bot" ? "bot-message" : "user-message"
          }`}
        >
          {message.text && <p>{message.text}</p>}
          {message.imageUrl && (
            <img
              src={message.imageUrl}
              alt="Bot response"
              className="message-image"
            />

          )}
        </div>
      ))}
      {isLoading && (
        <div className="message bot-message">
          <Spinner />
        </div>
      )}
    </div>
  );
};

export default MessageList;
