import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ApplicationsPageComponent } from './applications-page/applications-page.component';
import { NewApplicationComponent } from './new-application/new-application.component';

const routes: Routes = [
  { path: 'applications', component: ApplicationsPageComponent },
  { path: 'applications/new', component: NewApplicationComponent },
  // { path:}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
