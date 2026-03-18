import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Businesses } from './components/businesses/businesses';
import jsonData from '../app/assets/business.json';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Businesses],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('BIZFE');
  ngOnInit() {
    console.log(jsonData);
  }
}
