import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router'
import { OverviewPageComponent } from './overview-page/overview-page.component';

const routes: Routes = [
  { path: 'overview', component:OverviewPageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
