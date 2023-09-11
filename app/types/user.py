from app.utils.dt import parse_datetime
from tweepy.user import User as TweepyUser


class User(TweepyUser):
    def __init__(self, data):
        """
        parse a TimelineTimelineItem['content']['itemContent']['user_results']['result'] here
        """
        legacy = data['legacy'].copy()

        # Patches for Tweepy's User types
        legacy['id'] = data['rest_id']
        legacy['username'] = legacy['screen_name']
        legacy.pop('created_at')
        super().__init__(data=legacy)
        self.created_at = parse_datetime(data['legacy']['created_at'])

        """
        Already defined:
        [
            "created_at",
            "description",
            "entities",
            "id",
            "location",
            "name",
            "pinned_tweet_id",
            "profile_image_url",
            "protected",
            "public_metrics",
            "url",
            "username",
            "verified",
            "verified_type",
            "withheld",
        ]
        """

        # counts
        self.favourites_count = legacy.get('favourites_count')
        self.followers_count = legacy.get('followers_count')
        self.friends_count = legacy.get('friends_count')
        self.listed_count = legacy.get('listed_count')
        self.statuses_count = legacy.get('statuses_count')
        self.media_count = legacy.get('media_count')

        # data['pinned_tweet_ids_str'][0]
        self.pinned_tweet_id = legacy.get('pinned_tweet_ids_str')[0] if legacy.get('pinned_tweet_ids_str') else None

        # urls
        self.profile_image_url = legacy.get('profile_image_url_https')
        self.profile_banner_url = legacy.get('profile_banner_url')

        # booleans
        self.possibly_sensitive = legacy.get('possibly_sensitive')
