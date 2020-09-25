import { Component, OnInit } from '@angular/core';
import { EmojiApi } from './services/emojis.api';
import { AuthApi } from './services/auth.api';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  constructor(private emojiApi: EmojiApi, private authApi: AuthApi) {}

  public emojis = [];
  public meals = [];
  public mealtimes = [];
  public selectedEmojis = [];
  public selectedMeal;
  public selectedMealTime;
  public searchInput = '';
  public pending = false;

  public currentStep = 'login';

  public username = '';
  public password = '';

  searchEmojis(query) {
    this.emojiApi.getEmojis(query).subscribe((emojis) => {
      this.emojis = emojis;
    });
  }

  isSelected(emoji) {
    return this.selectedEmojis.findIndex(e => e.emojiName === emoji.emojiName) !== -1;
  }

  select(emoji) {
    const i = this.selectedEmojis.findIndex(e => e.emojiName === emoji.emojiName);
    if (i === -1) {
      this.selectedEmojis.push(emoji);
    } else {
      this.selectedEmojis.splice(i, 1);
    }
  }

  proceed() {
    this.currentStep = 'finalize';
  }

  back() {
    this.currentStep = 'select-emoji';
  }

  reset() {
    this.selectedEmojis = [];
    this.selectedMeal = this.meals[0];
    this.selectedMealTime = this.mealtimes[0];
  }

  send() {
    this.pending = true;
    const user = localStorage.getItem('username');
    const emojis = this.selectedEmojis.map((emoji) => emoji.emojiName);
    this.emojiApi.postTestEntry(user,
       emojis,
       this.selectedMeal.mealName,
       this.selectedMealTime.mealTimeName).subscribe((resp) => {
        this.pending = false;
        this.reset();
        this.currentStep = 'success';
      });
  }

  login() {
    this.pending = true;
    this.authApi.login(this.username, this.password).subscribe((resp) => {
      localStorage.setItem('token', resp.token);
      localStorage.setItem('username', this.username);
      this.pending = false;
      this.currentStep = 'select-emoji';
      this.getEmojitestData();
    });
  }

  logout() {
    localStorage.clear();
    this.currentStep = 'login';
  }

  getEmojitestData() {
    this.searchEmojis('');
    this.emojiApi.getMeals().subscribe((meals) => {
        this.meals = meals;
        this.selectedMeal = meals[0];
      });
    this.emojiApi.getMealTimes().subscribe((mealtimes) => {
        this.mealtimes = mealtimes;
        this.selectedMealTime = mealtimes[0];
      });
  }

  ngOnInit() {

    if (localStorage.getItem('token')) {
      this.currentStep = 'select-emoji';
      this.getEmojitestData();
    }
  }

}
