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
  public selectedEmojis = [];
  public searchInput = '';

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

  ngOnInit() {
    this.searchEmojis('');
  }

}
