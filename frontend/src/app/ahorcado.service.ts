import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AhorcadoService {
  constructor(private http: HttpClient, private router: Router) {}

  private apiAhorcado = 'http://127.0.0.1:8000';

  public setPalabra(palabra: string | null): Observable<any> {
    return this.http.get<any>(`${this.apiAhorcado}/ingresa_palabra/${palabra}`);
  }

  public adivinarLetra(letra: string): Observable<any> {
    return this.http.get<any>(`${this.apiAhorcado}/adivina_letra/${letra}`);
  }

  public adivinarPalabra(palabra: string): Observable<any> {
    return this.http.get<any>(`${this.apiAhorcado}/adivina_palabra/${palabra}`);
  }

  public getPalabra(): Observable<any> {
    return this.http.get<any>(`${this.apiAhorcado}/get_palabra`);
  }

  public getVidas(): Observable<any> {
    return this.http.get<any>(`${this.apiAhorcado}/get_vidas`);
  }

  public getEstado(): Observable<any> {
    return this.http.get<any>(`${this.apiAhorcado}/get_estado`);
  }

  public getLetrasIncorrectas(): Observable<any> {
    return this.http.get<any>(`${this.apiAhorcado}/get_letras_incorrectas`);
  }
}
