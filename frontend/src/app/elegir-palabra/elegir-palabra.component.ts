import { Component } from '@angular/core';
import { AhorcadoService } from '../ahorcado.service';
import { FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-elegir-palabra',
  templateUrl: './elegir-palabra.component.html',
  styleUrls: ['./elegir-palabra.component.css'],
})
export class ElegirPalabraComponent {
  constructor(private as: AhorcadoService, private router: Router) {}

  palabra = new FormControl('', Validators.required);

  jugar() {
    const observer = {
      next: (resultado: any) => {
        localStorage.setItem('palabra', this.palabra.value!);
        this.router.navigate(['/ahorcado']);
      },
      error: (error: any) => {
        console.error('Error:', error);
      },
    };

    this.as.setPalabra(this.palabra.value!).subscribe(observer);
  }
}
