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

  public setPalabra(palabra: string): Observable<any> {
    return this.http.get<any>(`${this.apiAhorcado}/ingresa_palabra/${palabra}`);
  }

  public adivinarLetra(letra: string): Observable<any> {
    return this.http.get<any>(`${this.apiAhorcado}/adivina_letra/${letra}`);
  }
}
