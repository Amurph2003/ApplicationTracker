import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ApplicationsPageComponent } from './applications-page/applications-page.component';

const routes: Routes = [
  { path: 'applications', component: ApplicationsPageComponent },
  // { path:}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
