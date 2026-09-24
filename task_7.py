    # ==============================================================================
# TASK 7: Produce the weekly dispatch report
# ==============================================================================

def produce_weekly_report(deliveries_str, target):
    """
    Processes 7 daily delivery counts and a target value to print the weekly report.
    For ties, reports the LAST day with the highest/lowest value.
    """
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Split comma-separated string into integer list
    raw_parts = deliveries_str.split(",")
    deliveries = []
    for part in raw_parts:
        deliveries.append(int(part.strip()))
        
    # Manual manual traversal using accumulators
    total_deliveries = 0
    days_meeting_target = 0
    
    highest_val = deliveries[0]
    highest_day_idx = 0
    
    lowest_val = deliveries[0]
    lowest_day_idx = 0
    
    for i in range(len(deliveries)):
        val = deliveries[i]
        total_deliveries += val
        
        if val >= target:
            days_meeting_target += 1
            
        # >= and <= ensure that in case of ties, the LAST occurrence is kept
        if val >= highest_val:
            highest_val = val
            highest_day_idx = i
            
        if val <= lowest_val:
            lowest_val = val
            lowest_day_idx = i
            
    avg_per_day = total_deliveries / len(deliveries)
    
    # Print formatted summary report
    print("Weekly dispatch report")
    print(f"Total deliveries: {total_deliveries}")
    print(f"Average per day: {avg_per_day:.2f}")
    print(f"Highest day: {days[highest_day_idx]} ({highest_val})")
    print(f"Lowest day: {days[lowest_day_idx]} ({lowest_val})")
    print(f"Days meeting target: {days_meeting_target}")
