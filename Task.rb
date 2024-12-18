class Stack
    def initialize
        @list = []
        @max = []
        @sum = 0
    end

    def push(added_no)
        if added_no < 0 || !added_no.is_a?(Integer)
            raise ArgumentError, "Value must be a positive integer"
        end

        @list.push(added_no)
        @sum += added_no

        if @max.empty? || added_no > @max.last
            @max.push(added_no)
        end
    end

    def pop
        if @list.empty?
            return nil
        end
        
        removed_no = @list.pop
        @sum -= removed_no

        if removed_no == @max.last
            @max.pop
        end

        return removed_no
    end

    def max
        if @max.empty?
            return nil
        end

        return @max.last
    end

    def size
        return @list.size
    end

    def sum
        return @sum
    end
end

class Extras < Stack
    def average
        if size == 0
            return nil
        end

        return sum.to_f / size
    end
end


# Why is this solution fast?
# Beacuse all of methods are O(1) time complexity.

