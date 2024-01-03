import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AhorcadoComponent } from './ahorcado/ahorcado.component';
import { ElegirPalabraComponent } from './elegir-palabra/elegir-palabra.component';

const routes: Routes = [
  { path: '', redirectTo: '/jugar', pathMatch: 'full' },
  { path: 'jugar', component: ElegirPalabraComponent },
  { path: 'ahorcado', component: AhorcadoComponent },
  { path: '**', component: ElegirPalabraComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: [RouterModule],
})
export class AppRoutingModule {}
