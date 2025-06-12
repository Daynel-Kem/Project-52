import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import {FormsModule} from '@angular/forms'
import { ChatbotService } from '../../services/chatbot.service';
import { Message } from '../../app.component';

@Component({
  selector: 'app-chat-area',
  imports: [FormsModule],
  templateUrl: './chat-area.component.html',
  styleUrl: './chat-area.component.scss'
})
export class ChatAreaComponent {
  userMessage: string = "";
  botResponse: Message = {
    message: "",
    isUser: false,
  }

  messageSent: boolean = true;

  messages: Message[] = [
    {
      message: "Hello, how can I help you today?",
      isUser: false,
    }
  ];

  constructor(private chatBotService: ChatbotService) {}

  @ViewChild('chatContainer') chatContainer!: ElementRef;

  ngOnInit() {
    // Scroll to the bottom of the chat container when the component initializes
    this.scrollToBottom();
  }

  ngAfterViewChecked() {
    this.scrollToBottom()
  }

  scrollToBottom() {
    try {
      const el = this.chatContainer.nativeElement;
      el.scrollTop = el.scrollHeight;
    } catch (err) {
      console.error('Scroll error:', err);
    }
  }

  async addMessage() {
    const newMessage: Message = {
      message: this.userMessage,
      isUser: true,
    }
    this.messageSent = false

    this.messages.push(newMessage)
    this.userMessage = '';

    const response = await this.chatBotService.getResponse(this.messages)
    this.botResponse = response

    this.messages.push(this.botResponse)

    this.messageSent = true
  }
}

