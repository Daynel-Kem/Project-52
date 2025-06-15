import { Component } from '@angular/core';
import { ChatAreaComponent } from '../../components/chat-area/chat-area.component';
import { ModelComponent } from '../../components/model/model.component';

@Component({
  selector: 'app-chat-page',
  imports: [ChatAreaComponent, ModelComponent],
  templateUrl: './chat-page.component.html',
  styleUrl: './chat-page.component.scss',
  standalone: true,
})
export class ChatPageComponent {

}
