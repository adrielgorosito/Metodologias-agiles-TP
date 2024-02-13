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

  palabra = new FormControl('', [Validators.required, Validators.pattern(/^[A-Za-z]+$/)]);

  jugar() {
    const observer = {
      next: () => this.router.navigate(['/ahorcado']),
      error: () => alert("Error: tienes que ingresar una palabra."),
    };

    if (this.palabra.value!.length > 16)
      alert("La palabra debe ser de 16 caracteres o menos");
    else {
      this.as.setPalabra(this.palabra.value!.toLowerCase()).subscribe(observer);
    }
  }
}
