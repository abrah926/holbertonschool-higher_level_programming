class VerboseList(list):
    def append(self, item):
        print(f'Added {item!r} to the list')
        super().append(item)

    def extend(self, iterable):
        super().extend(iterable)
        print(f'Extended the list with {len(iterable)} items')

    def remove(self, item):
        if item in self:
            super().remove(item)
            print(f'Removed {item!r} from the list')
        else:
            print(f'{item!r} is not in the list')

    def pop(self, index=-1):
        item = super().pop(index)
        print(f'Removed {item!r} from the list')
        return item
