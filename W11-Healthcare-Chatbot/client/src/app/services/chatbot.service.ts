import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { firstValueFrom } from 'rxjs';
import { Message } from '../app.component';

@Injectable({
  providedIn: 'root'
})
export class ChatbotService {
  baseUrl = "http://127.0.0.1:5000"

  constructor(private http: HttpClient) { }

  async getResponse(messages: Object[]): Promise<any> {
    try {
      const response = await firstValueFrom(this.http.post<any>(`${this.baseUrl}/generate-response`, {"messages": messages}));
      return response
    } catch (error) {
      console.error('Error Fetching response from backend', error)
      throw error
    }

  }

}
