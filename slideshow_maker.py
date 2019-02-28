from slide import Slide


class SlideshowMaker(object):
    def __init__(self):
        # Maybe this will be useful
        pass

    def greedy_make(self, pics):
        slideshow = []

        previous_slide = None
        current_slide = None

        for i, pic in pics.items():
            # First, only Horizontal
            if pic.orientation == 1:
                continue

            if current_slide is None:
                current_slide = Slide(pic, None)
                continue

            if current_slide.is_valid():  # Horizontal
                if previous_slide is None:
                    slideshow.append(current_slide)
                    previous_slide = current_slide
                else:
                    if current_slide.tags & previous_slide.tags:
                        # Ok, current slide is valid, add it to slideshow
                        slideshow.append(current_slide)
                        previous_slide = current_slide

        return slideshow
