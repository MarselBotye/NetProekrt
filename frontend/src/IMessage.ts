interface Message {
  text: string;
  imageUrl?: string;
  sender: "user" | "bot";
}

export default Message;
