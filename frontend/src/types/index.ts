// TypeScript Interfaces for CareerPath AI

export interface UserProfile {
  userId: number;
  major?: string;
  educationLevel?: string;
  careerYears: number;
  skills: string[];
  certifications: string[];
  projects: { title: string; description: string; skills: string[] }[];
  targetJob?: string;
  targetIndustry?: string;
  targetLocation?: string;
  targetCompanySize?: string;
  prepPeriodMonths: number;
  psychologicalTestData?: Record<string, any>;
}

export interface JobRecommendation {
  jobCode: string;
  title: string;
  category?: string;
  aptitudeMatchScore: number;
  readinessScore: number;
  matchingReason: string;
  keySkills: string[];
}

export interface RecruitmentItem {
  recruitmentId: string;
  companyName: string;
  title: string;
  location?: string;
  companySize?: string;
  salaryInfo?: string;
  matchScore: number;
  fitReasons: string[];
  missingSkills: string[];
  detailUrl?: string;
}

export interface SkillGapItem {
  skillName: string;
  demandFrequency: number;
  isPossessed: boolean;
  priorityLevel: 'High' | 'Medium' | 'Low';
  learningWeeks: number;
  recommendedTrainings: string[];
  recommendedCertifications: string[];
}

export interface SkillGapAnalysis {
  targetJob: string;
  readinessRate: number;
  possessedSkills: string[];
  missingSkills: string[];
  skillBreakdown: SkillGapItem[];
}

export interface ActionPlanStep {
  weekRange: string;
  title: string;
  goal: string;
  recommendedActivities: string[];
  linkedTrainings: { name: string; source: string }[];
  linkedCertifications: { name: string; source: string }[];
}

export interface CareerRoadmap {
  id: number;
  userId: number;
  targetJob: string;
  totalWeeks: number;
  actionPlans: ActionPlanStep[];
  skillGapSummary: Record<string, any>;
}

export interface SimulationResult {
  activityName: string;
  durationWeeks: number;
  readinessBefore: number;
  readinessAfter: number;
  scoreDelta: number;
  description: string;
}

export interface AgentChatMessage {
  role: 'user' | 'assistant' | 'system';
  content: string;
}
