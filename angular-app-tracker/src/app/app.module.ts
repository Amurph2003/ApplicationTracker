import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ApplicationsPageComponent } from './applications-page/applications-page.component';
import { NewApplicationComponent } from './new-application/new-application.component';
import { UpdateApplicationComponent } from './update-application/update-application.component';
import { SignInPageComponent } from './sign-in-page/sign-in-page.component';
import { ApplicationDetailComponent } from './application-detail/application-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    ApplicationsPageComponent,
    NewApplicationComponent,
    UpdateApplicationComponent,
    SignInPageComponent,
    ApplicationDetailComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
