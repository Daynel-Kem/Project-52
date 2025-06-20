import {animate, query, style, transition, trigger} from '@angular/animations';

export const routeTransition = trigger('routeTransition', [
  transition('* => *', [
    query(':enter', [
        style({opacity: 0, transform: 'translateY(20px)'}),
    ], {optional: true}),
    query(':enter', [
        animate('300ms ease-out', style({opacity: 1, transform: 'translateY(0)'}))
    ], {optional: true})
  ])
]);