from functools import total_ordering

@total_ordering
class Version(object):
  def __init__(self, string):
    self.string = string
    self.converted = list(map(lambda v: int(v), string.split('.')))

  def __eq__(self, other):
    return self.string == other.string

  def __gt__(self, other):
    return self.major > other.major or \
      self.major == other.major and self.minor > other.minor or \
      self.major == other.major and self.minor == other.minor and self.revision > other.revision or \
      self.major == other.major and self.minor == other.minor and self.revision == other.revision and \
      self.size > other.size

  @property
  def size(self):
    return len(self.converted)

  @property
  def major(self):
    return self.converted[0]

  @property
  def minor(self):
    return self.converted[1] if self.size > 1 else 0

  @property
  def revision(self):
    return self.converted[2] if self.size > 2 else 0


def solution(l):
  return sorted(l, key=Version)
