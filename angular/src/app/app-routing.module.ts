import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SomethingCoolComponent } from './something-cool/something-cool.component';

const routes: Routes = [
  {
    path: 'something-cool',
    component: SomethingCoolComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
