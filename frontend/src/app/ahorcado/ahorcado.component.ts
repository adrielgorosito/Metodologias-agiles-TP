import { Component } from '@angular/core';
import { FormBuilder, FormControl, Validators } from '@angular/forms';
import { AhorcadoService } from '../ahorcado.service';

@Component({
  selector: 'app-ahorcado',
  templateUrl: './ahorcado.component.html',
  styleUrls: ['./ahorcado.component.css'],
})
export class AhorcadoComponent {
  constructor(private as: AhorcadoService) {}

  letra = new FormControl('', Validators.required);

  palabra = localStorage.getItem('palabra');
  palabraConGuionesBajo: string = this.palabra!.split('')
    .map(() => '_')
    .join('')
    .split('')
    .join(' ');

  adivinarLetra() {
    const observer = {
      next: (resultado: any) => {
        if (resultado === false)
          console.log('La letra no se encuentra en la palabra.');
        else {
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
}
