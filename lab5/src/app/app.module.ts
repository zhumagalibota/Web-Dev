import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser'; // Import BrowserModule
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule // Add BrowserModule to imports array
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
