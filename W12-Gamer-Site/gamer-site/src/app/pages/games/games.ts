import { Component } from '@angular/core';

@Component({
  selector: 'app-games',
  imports: [],
  templateUrl: './games.html',
  styleUrl: './games.scss'
})
export class Games {
  games: Game[] = [];
  
}

interface Game {
  id: number;
  name: string;
  description: string;
  releaseDate: string;
  genre: string;
  imageUrl: string;
}
