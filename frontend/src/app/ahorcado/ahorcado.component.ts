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
  palabraArriesgada = new FormControl('', Validators.required);
  gano: boolean = false;
  palabra: string = '';
  palabraConGuionesBajo: string = '';
  vidas: number = 7;
  letrasIncorrectas: string = '';

  ngOnInit(): void {
    this.as.getPalabra().subscribe((p: string) => this.palabra = p);
    this.as.getEstado().subscribe((p: string[]) => this.palabraConGuionesBajo = p.join(' '));
    this.as.getVidas().subscribe((vidas: number) => this.vidas = vidas);
    this.as.getLetrasIncorrectas().subscribe((letras: string[]) => this.letrasIncorrectas = letras.join(' '));
  }

  adivinarLetra() {
    const observer = {
      next: (resultado: any) => {
        if (resultado === false && !this.letrasIncorrectas.includes(this.letra.value!)) {
          this.as.getVidas().subscribe((vidas: number) => this.vidas = vidas);
          this.as.getLetrasIncorrectas().subscribe((letras: string[]) => this.letrasIncorrectas = letras.join(' '));
        } else {
          this.as.getEstado().subscribe((estado: string[]) => {
            this.palabraConGuionesBajo = estado.join(' ');
            const p = this.palabraConGuionesBajo.split(' ').map((c) => c === '_' ? ' ' : c).join('');
            
            if (p == this.palabra) {
              this.vidas = 0;
              this.gano = true;
            }
          });
        }
      },
      complete: () => this.letra.reset(),
    };

    this.as.adivinarLetra(this.letra.value!.toLowerCase()).subscribe(observer);
  }

  adivinarPalabra() {
    const observer = {
      next: (resultado: any) => resultado === true ? this.gano = true : this.gano = false,
      complete: () => this.vidas = 0,
    };

    this.as.adivinarPalabra(this.palabraArriesgada.value!.toLowerCase()).subscribe(observer);
  }

  reiniciar() {
    this.as.setPalabra(null).subscribe(() => this.router.navigate(['/jugar']));
  }
}