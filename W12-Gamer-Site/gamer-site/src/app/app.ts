import { Component } from '@angular/core';
import { ActivatedRoute, RouterModule, RouterOutlet } from '@angular/router';
import { Navbar } from './components/navbar/navbar';
import { Footer } from './components/footer/footer';
import { routeTransition } from './transitions/route-transition';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterModule, Navbar, Footer],
  templateUrl: './app.html',
  styleUrl: './app.scss',
  animations: [
    routeTransition
  ]
})
export class App {
  protected title = 'gamer-site';

  constructor(public route: ActivatedRoute) {}
}
