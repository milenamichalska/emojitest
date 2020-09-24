import { Component, OnInit } from '@angular/core';
import { EmojiApi } from './services/emojis.api';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  constructor(private emojiApi: EmojiApi) {}

  public emojis = [];
  public meals = [];
  public mealtimes = [];
  public selectedEmojis = [];
  public selectedMeal;
  public selectedMealTime;
  public searchInput = '';
  public pending = false;

  public currentStep = 'select-emoji';

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

  send() {
    this.pending = true;
    this.emojiApi.postTestEntry(this.selectedEmojis, this.selectedMeal, this.selectedMealTime).subscribe((resp) => {
      console.log(resp);
    })
  }

  ngOnInit() {
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

}
