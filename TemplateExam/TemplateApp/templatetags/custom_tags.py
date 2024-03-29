from django import template
from datetime import datetime
import math

register = template.Library();

@register.filter(name='time_since_joined')
def time_since_joined(value):
  join_datetime = datetime.strptime(value, '%Y/%m/%d')
  now_datetime = datetime.now()
  diff_datetime = now_datetime - join_datetime
  diff_days = diff_datetime.days
  diff_years = math.floor(diff_days / 365)
  diff_months = math.floor((diff_days - 365 * diff_years) / 30)
  return f'{diff_years} year {diff_months} month'