import { Component } from '@angular/core';
import { FormBuilder, FormControl, Validators } from '@angular/forms';
import { AhorcadoService } from '../ahorcado.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-ahorcado',
  templateUrl: './ahorcado.component.html',
  styleUrls: ['./ahorcado.component.css'],
})
export class AhorcadoComponent {
  constructor(private as: AhorcadoService, private router: Router) {}

  letra = new FormControl('', Validators.required);

  palabra = localStorage.getItem('palabra');
  palabraConGuionesBajo: string = this.palabra!.split('')
    .map(() => '_')
    .join('')
    .split('')
    .join(' ');
  vidas: number = 7;
  letrasErradas: string[] = [];

  adivinarLetra() {
    const observer = {
      next: (resultado: any) => {
        if (
          resultado === false &&
          !this.letrasErradas.includes(this.letra.value!)
        ) {
          this.vidas--;
          this.letrasErradas.push(this.letra.value!);
        } else {
          resultado.forEach((posicion: number) => {
            this.palabraConGuionesBajo = this.actualizarPalabraConGuionesBajo(
              resultado,
              this.palabraConGuionesBajo,
              this.letra.value!
            );
          });
        }
      },
      error: (error: any) => {
        console.error('Error:', error);
      },
      complete: () => {
        this.letra.reset();
      },
    };
    this.as.adivinarLetra(this.letra.value!).subscribe(observer);
  }

  actualizarPalabraConGuionesBajo(
    posiciones: number[],
    cadena: string,
    letra: string
  ): string {
    const arrayPalabra = cadena.split(' ');
    posiciones.forEach((posicion: number) => {
      arrayPalabra[posicion - 1] = letra;
    });
    return arrayPalabra.join(' ');
  }

  reiniciar() {
    localStorage.removeItem('palabra');
    this.router.navigate(['/jugar']);
  }
}
