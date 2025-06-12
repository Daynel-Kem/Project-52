import { Component } from '@angular/core';
import { RouterModule, RouterOutlet } from '@angular/router';
import { ChatPageComponent } from './pages/chat-page/chat-page.component';


@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'client';
}

export interface Message {
  message: string;
  isUser: boolean;
}