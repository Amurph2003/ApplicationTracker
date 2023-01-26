import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ApplicationsPageComponent } from './applications-page/applications-page.component';
import { NewApplicationComponent } from './new-application/new-application.component';

@NgModule({
  declarations: [
    AppComponent,
    ApplicationsPageComponent,
    NewApplicationComponent
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
