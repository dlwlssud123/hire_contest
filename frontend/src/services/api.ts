import axios from 'axios';
import {
  UserProfile,
  JobRecommendation,
  RecruitmentItem,
  SkillGapAnalysis,
  CareerRoadmap,
  SimulationResult,
  AgentChatMessage
} from '../types';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const apiService = {
  // Profile
  getProfile: async (userId: number) => {
    const res = await apiClient.get<UserProfile>(`/profile/${userId}`);
    return res.data;
  },
  updateProfile: async (userId: number, data: Partial<UserProfile>) => {
    const res = await apiClient.post<UserProfile>(`/profile/${userId}`, data);
    return res.data;
  },

  // Jobs & Recruitments
  getJobRecommendations: async (userId: number) => {
    const res = await apiClient.get<{ user_id: number; recommendations: JobRecommendation[] }>(`/jobs/recommendations/${userId}`);
    return res.data;
  },
  searchRecruitments: async (jobTitle: string, region?: string) => {
    const res = await apiClient.get<{ items: RecruitmentItem[]; total: number }>('/recruitments/search', {
      params: { job_title: jobTitle, region },
    });
    return res.data;
  },

  // Skill Gap & Roadmap
  analyzeSkillGap: async (targetJob: string) => {
    const res = await apiClient.get<SkillGapAnalysis>('/skill-gap/analyze', {
      params: { target_job: targetJob },
    });
    return res.data;
  },
  optimizePath: async (targetJob: string, availableMonths: number) => {
    const res = await apiClient.post<CareerRoadmap>('/path/optimize', {
      target_job: targetJob,
      available_months: availableMonths,
    });
    return res.data;
  },

  // Simulation
  runSimulation: async (userId: number, targetJob: string, activities: string[]) => {
    const res = await apiClient.post('/simulation/simulate', {
      user_id: userId,
      target_job: targetJob,
      selected_activities: activities,
    });
    return res.data;
  },

  // Agent Chat
  chatWithAgent: async (userId: number, message: string, history: AgentChatMessage[], roadmapId?: number) => {
    const res = await apiClient.post('/agent/chat', {
      user_id: userId,
      message,
      conversation_history: history,
      current_roadmap_id: roadmapId,
    });
    return res.data;
  },

  // Report
  getCareerReport: async (userId: number, targetJob: string) => {
    const res = await apiClient.get('/reports/generate', {
      params: { user_id: userId, target_job: targetJob },
    });
    return res.data;
  },
};
